package main

import (
	"context"
	"log"
	"time"
	"github.com/coreos/etcd/clientv3"
)

func main() {
	ccfg := clientv3.Config{
		Endpoints:            []string{"10.10.25.24:2379"},
		DialTimeout:          1 * time.Second,
		DialKeepAliveTime:    1 * time.Second,
		DialKeepAliveTimeout: 500 * time.Millisecond,
	}
	cli, err := clientv3.New(ccfg)
	if err != nil {
		log.Print(err)
	}

	for
	{
		if _, err := cli.Put(context.TODO(), "foo-1", "bar-1"); err != nil {
			log.Print(err)
		}
		resp, err := cli.Get(context.TODO(), "foo-1")
		if err != nil {
                	log.Print(err)
        	} else {
        		log.Printf("Get is done. Metadata is %q\n", resp)
		}
		<-time.After(5*time.Second)
	}
	defer cli.Close()
}
