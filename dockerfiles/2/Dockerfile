FROM golang

WORKDIR /app
ADD . /app
RUN go build -o utopia

ENTRYPOINT ./utopia 
