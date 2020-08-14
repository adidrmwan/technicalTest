from behave import *
from itertools import islice

@given(u'This Number for {input} to Intersection Function')
def step_impl(context, input):
    Input = [int(i) for i in input.split(',')]
    context.input = [int(j) for j in islice(Input, len(Input)-1)]
    #uncomment 9th line for check the first input 
    print(context.input) 

@when(u'Asked to Find the Intersection for {number}')
def step_impl(context, number):
    Number = [int(i) for i in number.split(',')]    
    context.number = Number
    #uncomment 16th line for check the second input
    print(context.number)

@then(u'The Intersections Are {output}')
def step_impl(context, output):
    Output = [int(i) for i in output.split(',')]
    context.output = Output
    
    result_set = set()
    checked_set = set()
    for i in context.input:
        if i not in checked_set:
            checked_set.add(i)
            for j in context.number:
                if i == j :
                    result_set.add(i)
    result = list(result_set)
    print ('the result is :',result )

    # assert result == Output