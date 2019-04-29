import torch
from torch import nn
import torch.nn.functional as F
import torchvision
from torchvision import datasets, transforms, models
from torch.autograd import Variable
import subprocess

data_dir = "./data/actual"
input_size = 224
num_classes = 24

batch_size = 1
test_transforms = transforms.Compose([transforms.Resize(input_size),      
                                     transforms.CenterCrop(input_size),
                                     transforms.ToTensor(),
                                      transforms.Normalize([0.485, 0.456, 0.406],
                                                           [0.229, 0.224, 0.225])
                                     ])
image_dataset = datasets.ImageFolder(data_dir, test_transforms)
trainloader = torch.utils.data.DataLoader(image_dataset, batch_size=batch_size, shuffle=True, num_workers=4)

model = torch.load('./model.pth',map_location='cpu')
model.eval()

classes = ['ByrumHall', 'DeckerHall','DunnHall','EternalFlame',
           'FineArts','InternationalPlaza','HardacreHall','HartungHall','Helios',
           'KardatzkeWellnessCenter','NicholsonLibrary','MartinHall','MorrisonHall',
           'MyersHall', 'OLTStudentCenter','Passages','PeacePole','CentennialPrayerLabyrinth',
           'ReardonAuditorium','RiceHall','PioneerRock','CampusSeal','SmithHall','MorrisonStatue']

dataiter = iter(trainloader)
images, labels = dataiter.next()

outputs = model(images)
sm = torch.nn.Softmax(dim=1)
probs = sm(outputs)[0]
_, predicted = torch.max(outputs, 1)
maxx = probs[predicted].data[0]
command = 'html/' + classes[predicted[0]] + '.html'
subprocess.run(args=['cp',command, 'landmark.html'])
subprocess.run(args=['rm', 'data/actual/environment/run.jpg'])
print('\n{}, {}%\n'.format(classes[predicted[0]], maxx*100))
