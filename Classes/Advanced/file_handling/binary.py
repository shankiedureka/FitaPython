#sender
with open('E:/Git/FitaPython/Classes/Advanced/file_handling/sample.png','rb') as f:
    image_data = f.read()
print('done')
#Sending the image_data through some mode


#Receiver
#receiving the image_data
with open('E:/Git/FitaPython/Classes/Advanced/file_handling/sample_1.png','wb') as f:
    f.write(image_data)

# My storage - 64
# 50gb of original data
# Phone will have backup for all
# Convert to binary and store (5gb)