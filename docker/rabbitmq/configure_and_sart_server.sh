sleep 1; rabbitmq-server &
sleep 15; rabbitmqctl await_startup --timeout 300;
echo START IMPORT;
rabbitmqctl import_definitions /etc/rabbitmq/definitions_after_run.json;
echo IMPORT SUCCESS;
echo START CONFIGURE NETWORK;
# apt-get update
# apt-get -qq -y install curl
# apt-get install -y tc
# apt-get install -y iproute2
tc qdisc add dev eth0 root tbf rate 100kbps latency 50ms burst 2500;
echo CONFIGURE SUCCESS;
while :
do
sleep 10
done
