from telnetlib import STATUS
from unittest import result
import docker

class DockerHandling:
    def __init__(self,docker_url='unix://var/run/docker.sock'):
        try:
            self.client = docker.DockerClient(base_url=docker_url)
        except:
            return False

    def dockerimagespull(self,dockerImageName):
        try:
            img = self.client.images.pull(dockerImageName)
            img_id = img.id
            img_tag = img.tags[0]
            return {
                'status': 0,
                'id':img_id,
                'tag': img_tag
            }
        except:
            return {
                'status':1
            }
           

    def dockerImagesRemove(self,dockerImageName):
        try:
            self.client.images.remove(image=dockerImageName,force=True)
            return {
                'status': 0
            }
        except:
            return {
                'status': 1
            }

    def dockerImageslist(self):
        list = self.client.images.list()
        imagelist = []
        count = 1
        for image in list:
            img_id = image.id
            img_tag = image.tags
            rs = {
                "count": count,
                "id": img_id,
                "tag": img_tag
            }
            imagelist.append(rs)
            count = count + 1
        return imagelist


    def dockerImagesBuild(self,filepath,tagname):
        try:
            self.client.images.build(path=filepath,tag=tagname)
            return {
                "status":0
            }
        except:
            return {
                "status":1
            }

    def dockerImagesSearch(self,imagename):
        count = 1
        resultList = []
        list = self.client.images.search(term=imagename)
        if list.__len__() == 0:
            print("No Image found")
        else:
            for image in list:
                op = {
                    'count':count,
                    'name':image['name'],
                    'description':image['description'],
                    'official':image['is_official']
                    }
                resultList.append(op)
                count = count+1
        return resultList

    def dockerCreateContainer(self,imageName,containerName=None,detachBool=True,tty=False,commands=None,ports=None,envs=None):
        try:
                self.container = self.client.containers.run(image=imageName,name=containerName,detach=detachBool,tty=tty,ports=ports,environment=envs,command=commands)        
                self.container.start()
                cont_id =  self.container.id
                cont_img = str(self.container.image)
                cont_name = self.container.name
                return {
                    "status":0,
                    "id": cont_id,
                    "name": cont_name,
                    "image": cont_img
                }

        except:
            return {
                'status': 1
            }

    def dockerStopContainer(self,contID):
        try:
           cont =  self.client.containers.get(contID)
           cont.stop()
           return {
               'status':0
           }
        except:
            return {
                'status':1
            }

    def dockerStartContainer(self,contID):
        try:
           cont =  self.client.containers.get(contID)
           cont.start()
           return {
               'status':0
           }
        except:
            return {
                'status':1
            }

    def dockerRemoveContainer(self,contID):
        try:
           cont =  self.client.containers.get(contID)
           cont.stop()
           cont.remove()
           return {
               'status':0
           }
        except:
            return {
                'status':1
            }
