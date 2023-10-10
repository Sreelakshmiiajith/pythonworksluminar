# def product(*args): # * etra number of parameters ine accept cheyyum
#     result=1
#     for num in args:
#         result*=num
#     return result
    
# print(product(1,2))

# def max_word(*args):
#     lengthy_words=max(args,key=lambda w:len(w))
#     return(lengthy_words)
# print(max_word("hello","goodmorning","evening"))

# def display_emp(**kwargs):
#     print(kwargs)
#     print(kwargs.get("name"))
# display_emp(name="harii",dept="hr",n_place="kochin",w_location="tvm",salary=24000)

def display_stud(**kwargs):
    print(kwargs)
    print(kwargs.get("name"))
    print(kwargs.get("course"))

display_stud(name="ravi",course="django",rol=1000,gender="male")