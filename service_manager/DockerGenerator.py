def create(dir,requirements):
    f = open(dir+'/Dockerfile','w+')
    f.write("FROM ubuntu\n")
    f.write("RUN mkdir /project\n")
    
    f.write("RUN apt-get update && \\ \n")
    f.write("    apt-get install -y python3 && \\ \n")
    f.write("    apt install -y python3-pip && \\ \n") 
    f.write("    cd /project\n") 
    # f.write("RUN pip install Flask && \\ \n")
    # f.write("    pip install Flask_restful && \\ \n")
    # f.write("    pip install pickle-mixin && \\ \n") 
    # f.write("    pip install sklearn && \\ \n") 
    # f.write("    pip install dill \n") 
    
    # i=0
    # while i < len(requirements):
    #     if i == 0:
    #         f.write("RUN ")
    #     else :
    #         f.write("    ")
    #     f.write("pip install ")
    #     f.write(requirements[i])
    #     if i < len(requirements) - 1:
    #         f.write(" && \\ \n")
    #     else:
    #         f.write("\n")
    #     i+=1

    f.write("RUN ls project/ \n")
    f.write("ADD . /project/\n")
    f.write("WORKDIR /project/ \n")
    #install requrements file
    f.write("RUN pip install -r requirements.txt \n")
    f.write("EXPOSE 5000 \n")
    f.write('ENTRYPOINT ["python3" , "ModelInterface.py"] \n')
    f.close()
if __name__ == "__main__":
    create("hithr", ["lib1", "lib2"])
