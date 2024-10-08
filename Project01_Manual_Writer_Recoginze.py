#Project01：手写字体识别代码
#1、加载必要的库
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributed.pipelining import pipeline
from torchvision import datasets,transforms

#2、定义超参数
BATCH_SIZE = 16 #每批处理的数据
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu") #是否用CPU还是GPU训练
EPOCHS = 10 #训练数据集轮次

#3、构建pipeline，对图像转换
pipeline = transforms.Compose([
    transforms.ToTensor(),  #将图片转换成tensor
    transforms.Normalize((0.1307,),(0.3081,)) #数据模型正则化，降低模型复杂度
])

#4、下载、加载数据集
from torch.utils.data import DataLoader

#下载数据集
train_set = datasets.MNIST("data",train=True,download=True,transform=pipeline)
test_set = datasets.MNIST("data",train=False,download=True,transform=pipeline)
#加载数据集
train_loader = DataLoader(train_set,batch_size=BATCH_SIZE,shuffle=True)
test_loader = DataLoader(test_set,batch_size=BATCH_SIZE,shuffle=True)

#额外插入代码，显示MNIST中图片
with open("D:\\05_Python\\01_Python\\python\\data\\MNIST\\raw\\t10k-images-idx3-ubyte","rb") as f:
    file = f.read()

image1 = [int(str(item).encode("ascii"),16) for item in file[16:16+784]]
print(image1)

import cv2
import numpy as np
#image1_np = np.array(image1,dtype=np.uint8).reshape(28,28,1)
image1_np = np.array(image1).astype(dtype=np.uint8).reshape(28,28,1)
print(image1_np.shape)

cv2.imwrite("digit.jpg",image1_np)

#5、构建网络模型
class Digit(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1,10,5)  #1：灰度图片通道，10：输出通道，5：kernel
        self.conv2 = nn.Conv2d(10,20,3) #10：输入通道，20：输出通道，3：kernel
        self.fc1 = nn.Linear(20*10*10,500)  #20*10*10：输入通道，500：输出通道
        self.fc2 = nn.Linear(500,10) #500：输入通道，10：输出通道

    def forward(self,x):
        input_size = x.size(0) #batch_size x 1 x 28 x 28
        x = self.conv1(x) #输入：batch*1*28*28，输出：batch*10*24*24 (28-5+1=24)
        x = F.relu(x) #激活函数，输出：batch*10*24*24
        x = F.max_pool2d(x,2,2) #池化层，图片压缩，输入：batch*10*24*24，输出：batch*10*12*12

        x = self.conv2(x) #输入：batch*10*12*12，输出：batch*20*10*10 （12-3+1=10）
        x = F.relu(x) #激活函数

        x = x.view(input_size,-1) #图片拉直拉平，-1：自动计算维度：20*10*10

        x = self.fc1(x) #输入：batch*2000，输出：batch*500
        x = F.relu(x) #激活，爆出不变

        x = self.fc2(x) #输入：batch*500，输出：batch*10

        output = F.log_softmax(x,dim=1) #损失函数，计算分类后，每个数字的概率值

        return output

#6、定义优化器
model = Digit().to(DEVICE)
optimizer = optim.Adam(model.parameters())

#7、定义训练函数
def train_model(model,device,train_loader,optimizer,epoch):
    #模型训练
    model.train()
    for batch_index, (data, target) in enumerate(train_loader):
        #部署到device
        data,target = data.to(device), target.to(device)
        #梯度初始化为0
        optimizer.zero_grad()
        #预测训练后的结果
        output = model(data)
        #计算损失
        loss = F.cross_entropy(output,target)
        #找到概率值最大的下标
        #pred = output.max(1,keepdim=True)
        #pred = output.argmax(dim=1)
        #反向传播
        loss.backward()
        #参数优化
        optimizer.step()
        if batch_index % 3000 == 0:
            print("Train Epoch: {} \t Loss: {:.6f}".format(epoch,loss.item()))

#8、定义测试方法
def test_model(model,device,test_loader):
    #模型验证
    model.eval()
    #正确率
    correct = 0.0
    #测试损失
    test_loss = 0.0

    with torch.no_grad():  #不会计算梯度，也不会反向传播
        for data,target in test_loader:
            #部署到device上
            data,target = data.to(device),target.to(device)
            #测试数据
            output = model(data)
            #计算测试损失
            test_loss += F.cross_entropy(output,target).item()
            #找到概率值最大的下标
            pred = output.max(1,keepdim=True)[1] #值，索引
            #pred = torch.max(output,dim=1)
            #pred = output.argmax(dim=1)
            #累计正确率
            correct += pred.eq(target.view_as(pred)).sum().item()
        test_loss /= len(test_loader.dataset)
        print("Test --- Average loss: {:.4f}, Accuracy: {:.3f} \n".format(test_loss,100.0*correct /len(test_loader.dataset)))

#9、调用方法，输出结果
for epoch in range(1,EPOCHS+1):
    train_model(model,DEVICE,train_loader,optimizer,epoch)
    test_model(model,DEVICE,test_loader)
