package main

import (
	//"fmt"
	"context"
	"log"
	"time"
	"google.golang.org/grpc"
	healthpb "google.golang.org/grpc/health/grpc_health_v1"
)

func main() {
	conn, err := grpc.Dial("10.10.25.24:2379", grpc.WithInsecure())
	if err != nil {
		log.Printf("error to connect: %v", err)
	}
	defer conn.Close()
	cli := healthpb.NewHealthClient(conn)
	for {
		resp, err := cli.Check(context.Background(), &healthpb.HealthCheckRequest{})
		if err != nil {
			log.Printf("can not connect to the etcd server: %v, code: %v\n", err, grpc.Code(err))
		} else {
			log.Println("connected to the etcd server successfully")
		}
		log.Println(resp.Status)
		<-time.After(5*time.Second)
	}
}
