import Backend.dockerHandling as dockerHandling

object = dockerHandling.DockerHandling('tcp://192.168.56.106:2700')

# op = object.dockerImagesBuild("C:\\Users\\ayush\\Desktop\\test\\","myimg")
op = object.dockerImageslist()
print(op)