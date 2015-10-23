'''
Below links have the Google Code Jam qualification round practice problems. 
1. https://code.google.com/codejam/contest/351101/dashboard#s=p0
2. https://code.google.com/codejam/contest/351101/dashboard#s=p1
'''

#1st Problem - Store Credit
def solve(path,out):
    f = open(path, 'r')
    o = open(out, 'w')
    
    test_cases = int(f.readline())
    
    for c in range(test_cases):
        credit = int(f.readline())
        items = int(f.readline())  
        nos = map(int, f.readline().rstrip().split(' '))

        for i in range(items):
            for j in range(i+1, items):
                if nos[i] + nos[j] ==credit:
                    o.write('Case #{}: {} {}\n'.format(c+1, i+1, j+1))
                    break
    f.close()
    o.close()

# Replace with your file input and output paths 
solve('C:\Users\my\Desktop\A-Large-practice.in',
      'C:\Users\my\Desktop\A-Large-practice.out')




# 2nd Problem - Reverse words
def solve(path,out):
    f = open(path, 'r')
    o = open(out, 'w')    
        
    test_cases = int(f.readline())
    
    for c in range(test_cases):
        line = f.readline().split()
        print line
        print 'Case #{}: {}\n'.format(c+1, ' '.join(line[::-1]))
        o.write('Case #{}: {}\n'.format(c+1, ' '.join(line[::-1])))
    
#replace with your file input and output paths
solve('C:\Users\my\Desktop\B-large-practice.in',
      'C:\Users\my\Desktop\B-large-practice.out')









