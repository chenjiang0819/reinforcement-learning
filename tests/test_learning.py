from pathlib import Path
import ast,copy,random,unittest
import nbformat
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
def functions():
    nb=nbformat.read(ROOT/'Main.ipynb',as_version=4)
    ns={'np':np,'random':random,'choice':random.choice,'gridsize':2}
    for cell in nb.cells:
        if cell.cell_type!='code':continue
        tree=ast.parse('\n'.join(line for line in cell.source.splitlines() if not line.lstrip().startswith('%')))
        defs=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name!='generate_world']
        exec(compile(ast.Module(body=defs,type_ignores=[]),'notebook-functions','exec'),ns)
    return ns

class LearningTests(unittest.TestCase):
    def test_legal_action_indexing(self):
        ns=functions();q={i:[0.,0.,0.,0.] for i in range(4)};q[1]=[999.,1.,5.,0.]
        states,actions=ns['get_next_states'](1,0,2)
        value,action=ns['get_maxQ'](1,0,q,states,actions)
        self.assertEqual((value,action),(5.,2))

    def test_terminal_bootstrap(self):
        ns=functions();q={i:[0.,0.,0.,0.] for i in range(4)};q[0][0]=2.
        rewards=np.zeros((2,2));rewards[1,0]=1
        ns['QLearning'](rewards,q,gridsize=2,alpha=0,learning_rate=1,epochs=1,max_steps=1)
        self.assertEqual(q[0][0],1.)

    def test_step_cap_and_repeatability(self):
        ns=functions();base={i:[0.,0.,0.,0.] for i in range(9)};reward=np.zeros((3,3))
        a=ns['QLearning'](reward,copy.deepcopy(base),gridsize=3,epochs=5,max_steps=7,seed=42)
        b=ns['QLearning'](reward,copy.deepcopy(base),gridsize=3,epochs=5,max_steps=7,seed=42)
        self.assertEqual(a,b)
        self.assertTrue(all(len(t)==8 for t in a[1]))

    def test_small_goal_and_invalid_configuration(self):
        ns=functions();reward=np.zeros((3,3));reward[2,2]=1
        q={i:[0.,0.,0.,0.] for i in range(9)}
        _,paths=ns['QLearning'](reward,q,gridsize=3,epochs=200,max_steps=100,seed=7)
        self.assertGreater(sum(path[-1]==(2,2) for path in paths),150)
        with self.assertRaises(ValueError):ns['QLearning'](reward,q,gridsize=3,max_steps=0)
        with self.assertRaises(ValueError):ns['QLearning'](reward,{},gridsize=3)
        self.assertEqual(ns['get_next_states'](0,0,3)[1],[0,1])

if __name__=='__main__':unittest.main()
