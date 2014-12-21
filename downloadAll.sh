download_from_ips() {
    for THIRD_QUADRANT in $(seq 1 256)
    do
        for FOURTH_QUADRANT in $(seq 1 256)
        do
            IP_ADDRESS="178.62.${THIRD_QUADRANT}.${FOURTH_QUADRANT}"                            
            if wget --spider --quiet --connect-timeout=5 --tries=2 $IP_ADDRESS
            then
                wget --quiet -O $IP_ADDRESS --connect-timeout=5 --tries=2 $IP_ADDRESS &
                sleep 4
                kill $!           
            fi
        done
    done
}

download_from_ips