#!/usr/bin/env python3
from constraint import Problem ,AllDifferentConstraint , ExactSumConstraint

# Task 1    
def Travellers(List):
    problem = Problem ()
    people = [ "claude" , "olga" , "pablo" , "scott" ]
    times = [ "2:30" , "3:30" , "4:30" , "5:30" ]
    destinations = [ "peru" , "romania", "taiwan" , "yemen" ]
    t_variables = list ( map ( lambda x : "t_" +x , people ))
    d_variables = list ( map ( lambda x : "d_" +x , people ))
    problem.addVariables(t_variables , times)
    problem.addVariables(d_variables , destinations)
    problem.addConstraint(AllDifferentConstraint() , t_variables)
    problem.addConstraint(AllDifferentConstraint() , d_variables)
    for i in range(len(List)):
        n=List[i][0]
        t=List[i][1]
        problem.addConstraint(
            (lambda x,t=t : (x == t)),
            ["t_"+n])
    for person in people:
        
        # Olga is leaving 2 hours before the traveller from Yemen .
        # problem.addConstraint (
        #     ( lambda x ,y , z : ( y != "yemen" ) or
        #         (( x == "4:30" ) and ( z == "2:30" )) or
        #         (( x == "5:30" ) and ( z == "3:30" ))) ,
        #     [ "t_" + person , "d_" + person , "t_olga"])
        problem.addConstraint (
            ( lambda x :  (x == "2:30") or (x == "3:30")),
            ["t_claude"])
        problem.addConstraint (
            ( lambda x,y : ( x != "2:30") or 
                (y == "peru")),      
            [ "t_"+ person,"d_"+person])
        problem.addConstraint(
            ( lambda x,y : (y != "taiwan") or (x == "5:30")),
                ["t_"+person,"d_"+person])
        problem.addConstraint(
            ( lambda x,y : (y != "yemen") and ((x != "2:30") and (x != "3:30"))),
                ["t_pablo","d_pablo"])
        problem.addConstraint(
            ( lambda x,y : (y != "yemen") or ((x != "2:30") and (x != "3:30"))),
                ["t_"+person,"d_"+person])
       

    solns = problem.getSolutions ()
    return solns
   


# Task 2
def CommonSum(n):
    return ((n*(n**2+1))/2)


# Task 3
def msqList(n, pairList):
    problem = Problem()
    problem.addVariables(range (0,n * n) , range (1,n * n + 1))
    problem.addConstraint(AllDifferentConstraint() , range(0 , n * n ))
    for v, i in pairList:
        problem.addConstraint(ExactSumConstraint(i), [v])
    for row in range(n):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)) ,
            [row * n + i for i in range(n)])
    for col in range(n):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)),
            [col + n * i for i in range(n)])
    # Checking for main diagnols.
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i * n + i for i in range(n)])
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i * n + n - 1 - i for i in range(n)])

    return problem.getSolutions()


# Task 4
def pmsList(n, pairList):
    commonSum = CommonSum(n)

    problem = Problem ()
    problem.addVariables(range(0, n * n), range(1, n * n + 1))
    problem.addConstraint(AllDifferentConstraint(), range(0, n * n))

    for v, i in pairList:
        problem.addConstraint(ExactSumConstraint(i), [v])

    for row in range (n):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)), [row * n + i for i in range(n)])

    for col in range (n):
        problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i * n + col for i in range(n)])
    
    #checking for main diagnols
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i * n + i for i in range(n)])
    problem.addConstraint(ExactSumConstraint(CommonSum(n)), [i * n + n - 1 - i for i in range(n)])
    
    #checking for broken diagnols
    d= []
    dd = []
    #calculating downward broken diagnols
    for j in range(n-1):
        for i in range(n):
            d+=[i*n+i+(j+1)]
        dd+= [d]
        d = []


    for i in range(len(dd)-1,-1, -1): 
        ctr = 0
        l = dd[i]
      
        for j in range(n-i-1,len(dd)+1):
            l[j] = j*n + ctr
            ctr+=1
       
        dd[i] == l


    #calculating upward broken diagnols
    s=[]
    ss = []
    for i in range(n-1):
        for j in range(n):
            s+= [i*n - ((n-1)*j)]
        ss+=[s]
        s=[]



    for i in range(len(dd)-1,-1,-1):
       
        l1 = ss[i]
        ctr1 = 0
        for j in range(i+1,n):
         
            l1[j] = (n*n - n + i + 1) - ((n-1)*ctr1)
           
            ctr1+=1
        dd+=[l1]


   
    for i in range(len(dd)):
        problem.addConstraint(ExactSumConstraint(commonSum), dd[i])

    return problem.getSolutions()


# Debug
if __name__ == '__main__':
    print("debug run...")





