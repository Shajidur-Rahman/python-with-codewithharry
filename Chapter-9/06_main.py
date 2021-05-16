for j in range(1,20):
    with open(f'table/the{j}.txt' ,'w') as f:
        for i in range(1,11):
            t = f.write(f"{j} X {i} = {j*i}\n")
print('programe ran successfully')
