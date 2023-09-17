import {HealthItem} from "../Models/HealthItem";
import {Html5QrcodeScanner} from "html5-qrcode";
import {useEffect, useState} from "react";
import {Box, Center, useToast, Button, Heading, Spacer, VStack} from "@chakra-ui/react";
import {useNavigate} from "react-router-dom";
import * as React from "react";


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
        <VStack>
                <Heading
                    display="inline-block"
                    as="h2"
                    size="md"
                    bgGradient="linear(to-r, brand.300, brand.200)"
                    backgroundClip="text">
                    Health Harbor - Medicine Scanner
                </Heading>
                <Spacer height={20}/>
            <Box
                width={600}
                height={600}
            >
                <div id="reader"></div>
            </Box>
        </VStack>
    )
}