from torchvision.models import vgg16, vgg16_bn, vgg19, vgg19_bn, resnet18, resnet34, resnet50, resnet101, resnet152
from benchmarking import run_benchmarks

n_iters = 21
batch_size = 16

print("The models are being run on input size of {}".format((batch_size, 3, 224, 224)))
print("The time is the average over {} iterations".format(n_iters-1))
run_benchmarks([vgg16, vgg16_bn, vgg19, vgg19_bn, resnet18, resnet34, resnet50, resnet101, resnet152], batch_size, n_iters)