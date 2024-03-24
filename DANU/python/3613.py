def java_to_cpp(var_name):
    error = "Error!"
    
    converted_result = []
    
    for idx in range(len(var_name)):
        if var_name[idx].isupper():
            if idx == 0:
                return error
            else:
                converted_result.append(f"_{var_name[idx].lower()}")
        else:
            converted_result.append(var_name[idx].lower())
            
    return "".join(converted_result)


def cpp_to_java(var_name):
    error = "Error!"
    
    converted_result = []
    
    if "__" in var_name:
        return error
    if var_name[0] == "_" or var_name[-1] == "_":
        return error
    if not var_name.islower():
        return error
    
    for word in var_name.split("_"):
        if not converted_result:
            converted_result.append(word)
        else:
            converted_result.append(word.capitalize())
        
    return "".join(converted_result)


def main():
    var_name = input()
    
    if "_" in var_name:
        print(cpp_to_java(var_name=var_name))
    else:
        print(java_to_cpp(var_name=var_name))

if __name__ == "__main__":
    main()
