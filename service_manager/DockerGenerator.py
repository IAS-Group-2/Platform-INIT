def create(dir,requirements):
    f = open(dir+'/Dockerfile','w+')
    f.write("FROM python:3.6\n")
    f.write("RUN mkdir /project\n")
    
    f.write("RUN apt-get update && \\ \n")
    f.write("    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata &&  \\ \n")
    f.write("    apt-get install -y python3 && \\ \n")
    f.write("    apt install -y python3-pip && \\ \n") 
    f.write("    cd /project\n") 
    f.write("ADD . /project/\n")
    f.write("WORKDIR /project/ \n")
    #install requrements file
    f.write("RUN pip install -r requirements.txt \n")
    f.write("EXPOSE 5000 \n")
    f.write('ENTRYPOINT ["python3" , "ModelInterface.py"] \n')
    f.close()
if __name__ == "__main__":
    create("hithr", ["lib1", "lib2"])
