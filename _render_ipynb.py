#!python3
import json
import io

ipynb = open('test.ipynb').read()
for cell in json.loads(ipynb)['cells']:
    if cell['cell_type'] == 'markdown':
        for line in cell['source']:
            print(line)
        print()
        # source: 마크다운 내용, 각 줄(str)의 리스트
    elif cell['cell_type'] == 'code':
        print('['+str(cell['execution_count'])+']')
        for line in cell['source']:
            print('>>>', line.strip())
        print()
            
        output = cell['outputs']
        for out_cell in output:
            if out_cell['output_type'] == 'execute_result':
                print(out_cell['execution_count'],)
                for l in out_cell['data']:
                    if l == 'text/plain':
                        for txt in out_cell['data'][l]:
                            print(txt.strip())
                    elif l == 'text/html':
                        for txt in out_cell['data'][l]:
                            print(txt)
                print()
            elif out_cell['output_type'] == 'stream':
                for line in out_cell['text']:
                    print(line.strip())
            elif out_cell['output_type'] == 'error':
                print(out_cell['ename'] + ': ' + out_cell['evalue'])
                for line in out_cell['traceback']:
                    print(line)
            else:
                print('+'*50)
        print()
        # source: 코드 내용, 각 줄(str)의 리스트
        # outputs: 
        #   name: 아웃풋 이름 - stdout, 
        #   output_type: - stream
        #   text: - 아웃풋 내용, 각 줄의 리스트
        # execution_count: 실행 순서(int 혹은 null)
    elif cell['cell_type'] == 'raw':
        print(cell['source'])
        print()
        # source: 코드 내용, 각 줄(str)의 리스트
    else:
        print('+'*50)
        print(cell)
        print('='*50)
        print()
        
        
        

'''
프린트만 있는 셀
{
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6]\n",
      "[6, 5, 4, 3, 2, 1]\n"
     ]
    }
   ],
   "source": [
    "a = [6, 5, 4, 3, 2, 1]\n",
    "print merge_sort(a)\n",
    "print a"
   ]
  }

리턴만 있는 셀
{
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[1,2,3,4]"
   ]
  }

리턴, 프린트 있는 셀
{
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print (1,2,3,4)\n",
    "[1,2,3,4]"
   ]
  }
  
빈 셀
{
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }

rawnbconvert 셀  
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "gggggggg"
   ]
  }
'''
