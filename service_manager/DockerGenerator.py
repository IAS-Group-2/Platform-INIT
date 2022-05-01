def create(dir,apt_requirements,var_requirements):
    f = open(dir+'/Dockerfile','w+')
    f.write("FROM python:3.6\n")
    f.write("RUN mkdir /project\n")
    f.write("RUN apt-get update && \\ \n")
    # f.write("    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata &&  \\ \n")
    f.write("    apt-get install -y python3 && \\ \n")
    f.write("    apt install -y python3-pip && \\ \n") 
    # f.write("    apt-get install ffmpeg libsm6 libxext6 -y && \\ \n") 
    
    for var in var_requirements:
        f.write("    "+var+" && \\ \n")

    for requirement in apt_requirements:
        f.write("    apt-get install -y "+requirement+" && \\ \n")

    f.write("    cd /project\n")
    f.write("WORKDIR /project/ \n")
    f.write("COPY ./requirements.txt /project/requirements.txt\n")
    f.write("RUN pip install -r requirements.txt \n")
    f.write("COPY . /project/ \n")
    f.write("EXPOSE 5000 \n")
    f.write('ENTRYPOINT ["python3" , "ModelInterface.py"] \n')
    f.close()
    
# if __name__ == "__main__":
    # apt_reqs = ['tzdata','ffmpeg libsm6 libxext6']
    # var_reqs = ['DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC']
    # create("hithr", apt_reqs,var_reqs)
    # create("./", apt_reqs,var_reqs)
