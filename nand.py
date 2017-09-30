import sys
import os


# This function takes a text file with syntactic sugar, rewrites it in pure NAND
# and writes it to a test_converted.nand file. 

"""
CS121 HW2 2017
THE TODO's are optional, since you can choose which helper functions you want.
However, you must still come up with a way to meet the specification.
The included code helps make properly formated strings, opens and closes files,
and writes to files.
"""

'''
These make properly formated strings given triples of variables.
'''
def make_AND_statement(output,input1,input2,input3):
    return  "{} := {} AND {}".format(output, input1, input2)

def make_OR_statement(output,input1,input2):
    return  "{} := {} OR {}".format(output, input1, input2)

def make_XOR_statement(output,input1,input2):
    return  "{} := {} XOR {}".format(output, input1, input2)

def make_NAND_statement(output,input1,input2):
    return  "{} := {} NAND {}".format(output, input1, input2)


'''
Takes a file object f and a NAND line,
and writes a NAND line to the file with a newline character
'''
def write_NAND_line(f,line):
    f.write("%s\n" % line)

"""
Writes NAND triple (not line) to file
"""
def write_NAND_triple(f,output,x1,x2):
    line = make_NAND_statement(output,x1,x2)
    write_NAND_line(f,line)

'''
Writes any kind of line to file
'''
def write_DEBUG_line(f,line):
    f.write("%s\n" % line)


'''
Returns vars from OR line
'''
def parse_OR(line):
    # ASSUMES SPACING!
    vars = line.split()
    output = vars[0]
    input1 = vars[2]
    input2 = vars[4]
    return output, input1, input2


"""
Returns vars from XOR line
"""
def parse_XOR(line):
    # ASSUMES SPACING!
    # SAME FUNCTION AS parse_OR()
    vars = line.split()
    output = vars[0]
    input1 = vars[2]
    input2 = vars[4]
    return output, input1, input2

"""
Returns vars from AND line
"""
def parse_AND(line):
    # ASSUMES SPACING!
    # SAME FUNCTION AS parse_OR()
    vars = line.split()
    output = vars[0]
    input1 = vars[2]
    input2 = vars[4]
    return output, input1, input2

def parse_AND_TRIPLE(line):
    # ASSUMES SPACING!
    # SAME FUNCTION AS parse_OR()
    words = line.split()
    output = words[0]
    variables = words[2].split(',')
    index = variables[0].index('(')
    input1 = variables[0][index+1:]
    input2 = variables[1]
    input3 = variables[2][:len(variables[2]) - 1]
    return output, input1, input2, input3

"""
Returns vars from NAND line
"""
def parse_NAND(line):
	# ASSUMES SPACING!
	# SAME FUNCTION AS parse_OR() and parse_XOR()
	vars = line.split()
	output = vars[0]
	input1 = vars[2]
	input2 = vars[4]
	return output, input1, input2

"""
Returns vars from MAJ line
"""
def parse_MAJ(line):
    # ASSUMES SPACING!
    words = line.split()
    output = words[0]
    variables = words[2].split(',')
    index = variables[0].index('(')
    input1 = variables[0][index+1:]
    input2 = variables[1]
    input3 = variables[2][:len(variables[2]) - 1]
    return output, input1, input2, input3

"""
MOTIVATING QUESTION: WHY DO THE BELOW FUNCTIONS ALL TAKE A COUNTER ARGUMENT?
"""
def multiplyThree(input1,input2):
    return input2 * input2

'''
TODO: Implement a function that takes a number
and adds a special prefix to it
'''
def get_var_name(counter):
    #
    return "p_" + str(counter)

"""
Takes an AND line and writes a series of NAND lines to file
"""
def write_AND_as_NAND(f, line, counter):

    output,input0,input1 = parse_AND(line)

    u = get_var_name(counter)
    counter += 1

    write_NAND_line(f,u + " := " + input0 + " NAND " + input1)
    write_NAND_line(f,output+" := " + u + " NAND " + u)

    return counter

def write_AND_triple_as_NAND(f,line,counter):

    output,input0,input1,input2 = parse_AND_TRIPLE(line)

    u  = get_var_name(counter)
    counter += 1
    v = get_var_name(counter)
    counter += 1
    w = get_var_name(counter)
    counter+=1

    write_NAND_line(f,u + " := " + input0 + " NAND " + input1)
    write_NAND_line(f,v+" := " + u + " NAND " + u)
    write_NAND_line(f,w+" := " + v + " NAND " + input2)
    write_NAND_line(f,output+" := " + w + " NAND " + w)

    return counter


"""
Takes an XOR line and writes a series of NAND lines to file
"""
def write_XOR_as_NAND(f, line, counter):

    u  = get_var_name(counter)
    counter += 1
    v = get_var_name(counter)
    counter += 1
    w = get_var_name(counter)
    # counter += 1
    # y_0 = get_var_name(counter)

    write_NAND_line(f,u + " := " + parse_XOR(line)[1] + " NAND " + parse_XOR(line)[2])
    write_NAND_line(f,v + " := " + u + " NAND " + parse_XOR(line)[1])
    write_NAND_line(f,w + " := " +  u + " NAND " + parse_XOR(line)[2])
    write_NAND_line(f,parse_XOR(line)[0] + " := " + v + " NAND " + w)

    return counter

"""
Takes an OR line and writes a series of NAND lines to file
"""
def write_OR_as_NAND(f, line, counter):


    output,input1,input2 = parse_OR(line)

    u  = get_var_name(counter)
    counter += 1
    v = get_var_name(counter)
    counter+=1
    write_NAND_line(f,u + " := " + input1 + " NAND " + input1)
    write_NAND_line(f,v+" := " + input2 + " NAND " + input2)
    write_NAND_line(f,output+" := " + u + " NAND " + v)


    return counter

"""
Takes an OR triple and writes a series of NAND lines to file
"""
def write_OR_triple_as_NAND(f,output,input1,input2,counter):
    # TODO
    return counter

"""
Takes a MAJ line and writes a series of NAND lines to file
"""
def write_MAJ_as_NAND(fl, line,counter):
    # TODO	I WROTE HERE
    d  = get_var_name(counter)
    counter += 1
    e = get_var_name(counter)
    counter += 1
    f = get_var_name(counter)
    counter += 1
    g = get_var_name(counter)
    counter += 1
    h = get_var_name(counter)
    # counter += 1
    # i = get_var_name(counter)
    write_NAND_line(fl,d + " := " + parse_MAJ(line)[1] + " NAND " + parse_MAJ(line)[2])
    write_NAND_line(fl,e + " := " + parse_MAJ(line)[1] + " NAND " + parse_MAJ(line)[3])
    write_NAND_line(fl,f + " := " + parse_MAJ(line)[2] + " NAND " + parse_MAJ(line)[3])
    write_NAND_line(fl,g + " := " +  f + " NAND " + e)
    write_NAND_line(fl,h + " := " +  g + " NAND " + g)
    write_NAND_line(fl,parse_MAJ(line)[0] + " := " +  h + " NAND " + d)

    # (d,a,b),(e,a,c),(f,b,c),(g,f,e),(h,g,g),(i,h,d)
    return counter


"""
This function should:
    TODO: keep track of counter for new vars
    TODO: write an XOR line as a series of NAND lines
    TODO: write a MAJ line as a series of NAND lines
    TODO: leave NAND lines alone
"""
def NANDify(f,prog):
    counter = 0
    comments = 0
    for line in prog:
        if "XOR" in line:
            write_XOR_as_NAND(f, line, counter)
            counter +=4
        elif "MAJ" in line:
            write_MAJ_as_NAND(f, line, counter)
            counter+=6
        elif "OR" in line:
            write_OR_as_NAND(f,line,counter)
            counter+=1
        elif "AND" in line:
            write_AND_as_NAND(f,line,counter)
            counter+=1
        elif "AND_TRIPLE" in line:
            write_AND_triple_as_NAND(f,line,counter)
            counter+=3
        elif "//" in line:
            comments+=1
        else:
            write_NAND_line(f, line)


"""
usage: python NANDp2NAND.py "filename.nandp"
writes "filename_converted.nand"
"""
def main():
	inname = sys.argv[1]
	name,ext = os.path.splitext(inname)
	with open(inname,'r') as infile:
		prog = infile.readlines()
	outfile = open(name+'_converted.nand','w')
	NANDify(outfile,prog)
	outfile.close()

if __name__ == "__main__":
    main()
