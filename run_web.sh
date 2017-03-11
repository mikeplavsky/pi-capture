NAME=camera_web

docker build -t $NAME .

docker rm -f $NAME 
docker run -d \
    -v $(pwd):/web \
    -e FLASK_DEBUG=1 \
    --name=$NAME -p 5000:5000 $NAME

        
