from flask import Flask,jsonify,request
import os
# from werkzeug.utils import secure_filename
import Backend.dockerHandling as dockerHandling

app = Flask('dockerApp')
docker = dockerHandling.DockerHandling('tcp://192.168.56.106:2700')

@app.route("/pullimages",methods=["GET"])
def pullImages():
    imgname = request.args.get("imgname")
    result = docker.dockerimagespull(imgname)
    return jsonify(result)

@app.route("/removeimages",methods=["GET"])
def removeImages():
    imgname = request.args.get("imgname")
    result = docker.dockerImagesRemove(imgname)
    return jsonify(result)

@app.route("/listimages")
def listImages():  
    result = docker.dockerImageslist()
    return jsonify(result)

@app.route("/imagesearch",methods=["GET"])
def imageSearch():
    imgname = request.args.get("imgname")
    result = docker.dockerImagesSearch(imgname)
    return jsonify(result)

@app.route("/runcontainer",methods=["GET"])
def runContainers():
    imgname = request.args.get("imgname")
    containerName = request.args.get("name")
    detach = bool(request.args.get("detach"))
    tty = bool(request.args.get("tty"))
    cmd = request.args.get("cmd")
    ports = request.args.get("ports")
    if ports is not None:
        portsplit = ports.split(":")
        ports = {portsplit[1]+'/tcp':int(portsplit[0])}
    env = request.args.get("env")
    if env is not None:
        env = list(env.split(","))
    result = docker.dockerCreateContainer(imgname,containerName,detach,tty,cmd,ports,env)
    return jsonify(result)

# @app.route("/imagebuild", methods=['GET', 'POST'])
# def imageBuild():
#         tag = request.args.get("tag")
#         uploadPath= "C:\\Users\\ayush\\Desktop\\test"
#         if request.method=='POST':
#             f = request.files['file1']
#             f.save(os.path.join(uploadPath,secure_filename(f.filename)))
#             result = docker.dockerImagesBuild(uploadPath,tag)
#             return jsonify(result)

@app.route("/stopcontainer",methods=["GET"])
def stopContainer():
    contid = request.args.get("contid")
    result = docker.dockerStopContainer(contid)
    return jsonify(result)

@app.route("/startcontainer",methods=["GET"])
def startContainer():
    contid = request.args.get("contid")
    result = docker.dockerStartContainer(contid)
    return jsonify(result)


@app.route("/removecontainer",methods=["GET"])
def removeContainer():
    contid = request.args.get("contid")
    result = docker.dockerRemoveContainer(contid)
    return jsonify(result)


app.run(port=3000,debug=True)