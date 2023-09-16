import {HealthItem} from "../Models/HealthItem";
import {Html5QrcodeScanner} from "html5-qrcode";
import {useEffect, useState} from "react";
import {Box, Center, useToast, Button} from "@chakra-ui/react";
import {useNavigate} from "react-router-dom";


export const QrScanner = () => {

    const go_to_item_page = (item_id: string) => {
        window.location.pathname = "/item/" + item_id
    }

    useEffect(() => {

        const scanner = new Html5QrcodeScanner('reader', {
            qrbox: {
                width: 250,
                height: 250,
            },
            fps: 15
        }, false)

        function success(result: string) {
            go_to_item_page(result)
        }

        scanner.render(success, (err) => console.log(err))

    }, [])

    return (
        <Center>
            <Box
                width={600}
                height={600}
            >
                <div id="reader"></div>
            </Box>
        </Center>
    )
}