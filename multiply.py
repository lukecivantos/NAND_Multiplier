import sys
import os
import nand


# Multiply.py takes a text file and writes a NAND program (with AND and XOR 
# helpers) that multiplies two binary numbers of length n where n is the number 
# of binary digits in the call to 'genVars' within main.

# In order to get the NAND function, call genVars with two Binary digits of length
# 512 and have it write to test.text. Then call nand.py on test.text which removes
# all syntactic sugar. 
def genVars(f,input1,input2):
    strLen = len(input1) + len(input2)
    input1Vars = list(input1)
    input2Vars = list(input2)

    #ensure that longer string is first
    if len(input1Vars) < len(input2Vars):
        temp = input1Vars
        input1Vars = input2Vars
        input2Vars = temp


    nandCode = []
    multiLines = []

    # iterates the y variable which we save
    varCounter = 0
    for i in range(len(input2Vars)):
        accuum = []
        #add zero at beginning so
        for k in range(i):
            line = "p_"+str(varCounter)+" = zero AND zero"
            accuum.append("p_"+str(varCounter))
            varCounter+=1
            nand.write_NAND_line(f,line)
        for j in range(len(input1Vars)):
            # len(input1Vars)-j-1
            line = "p_"+str(varCounter)+" = x_"+str(strLen-i-1) + " AND " "x_"+str(len(input1Vars)-j-1)
            accuum.append("p_"+str(varCounter))
            varCounter+=1
            nand.write_NAND_line(f,line)
        for q in range(len(input2Vars)-i-1):
            line = "p_"+str(varCounter)+" =  zero AND zero"
            accuum.append("p_"+str(varCounter))
            varCounter+=1
            nand.write_NAND_line(f,line)
        # append zero to end of string so there is room for extra carry
        line = "p_"+str(varCounter)+" = zero AND zero"
        accuum.append("p_"+str(varCounter))
        varCounter+=1
        nand.write_NAND_line(f,line)
        multiLines.append(accuum)
    addVars(f,multiLines,varCounter)

# iteratively add each line to the current sum
def addVars(f,lineVars,counter):
    # need the first to be ripped off as initial sum
    currentSum = lineVars.pop(0)
    # print currentSum
    #iterate through rest of loop
    carry = "zero"
    # check if last iteration of loop
    isLast = False
    #used to name y vars
    yCounter = 0

    for i in range(len(lineVars)):
        if i == len(lineVars) - 1:
            isLast = True
        # placeholder for sum
        values = []
        for j in range(len(lineVars[i])):
            carry,value,yCounter = addBit(f,currentSum[j],lineVars[i][j],carry,counter,isLast,yCounter)
            counter+=5
            values.append(value)
        # set sum = to value
        currentSum = values
        # print lineVars[i],currentSum

def addBit(f,input1,input2,carry,counter,isLast,yCounter):
    u = counter
    counter +=1
    v = counter
    counter+=1
    w = counter
    counter+=1
    x = counter
    counter+=1
    y = counter
    counter+=1

    returnVal = "p_"+str(y)
    if isLast:
        returnVal = "y_"+str(yCounter)
        yCounter+=1

    nand.write_NAND_line(f, "p_"+str(u)+ " = " + input1 +" XOR " +input2)
    nand.write_NAND_line(f,"p_"+str(v)+" = "+ input1+" AND "+ input2)
    nand.write_NAND_line(f,"p_"+str(w) +" = "+carry +" AND " + "p_"+str(u))
    # print // Return Val to be carried
    nand.write_NAND_line(f,"p_"+ str(x) +" = "+ "p_"+str(v)+ " OR " +"p_"+str(w))
    # print // Return Val to be placed
    nand.write_NAND_line(f,returnVal+" = "+ carry +" XOR " +"p_"+str(u))

    # print "--------------------"

    return "p_"+str(x),"p_"+str(y),yCounter

def main():
	inname = sys.argv[1]
	name,ext = os.path.splitext(inname)
	outfile = open(name+'.text','w')
	genVars(outfile,'11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
    '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
	outfile.close()

if __name__ == "__main__":
    main()
