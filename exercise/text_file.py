'''
FROM nginx:alpine
COPY admin_pages /usr/share/nginx/html
EXPOSE 80
'''

#build docker image in terminal:
#       "docker build -t <tên image> . "    


#run docker container in terminal:
#       "docker run -d -p 8080:80 <tên image>"
#		"docker run -d -p 8081:80 --name <tên container> <tên image>"


#check các container đang chạy:
#       "docker ps"

#dừng container:
#       "docker stop <container_id>"

