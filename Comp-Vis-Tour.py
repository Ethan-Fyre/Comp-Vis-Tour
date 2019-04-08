import torch
from torch import nn
import torch.nn.functional as F
import torchvision
from torchvision import datasets, transforms, models
from torch.autograd import Variable

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

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.load('/home/jasayles/Comp-Vis-Tour/model.pth').to(device)
model.eval()

classes = ['Byrum Hall', 'Decker Hall','Dunn Hall','Eternal Flame',
           'Fine Arts','International Plaza','Hardacre Hall','Hartung Hall','Helios',
           'Kardatzke Wellnes Center','Nicholson Library','Martin Hall','Morrison Hall',
           'Myers Hall', 'OLT Student Center','Passages','Peace Pole','Centennial Prayer Labyrinth',
           'Reardon Auditorium','Rice Hall','Pioneer Rock','Campus Seal','Smith Hall','Morrison Statue']

dataiter = iter(trainloader)
images, labels = dataiter.next()

outputs = model(images.to(device))
_, predicted = torch.max(outputs, 1)

print('Predicted class is {}:'.format(classes[predicted[0]]))
