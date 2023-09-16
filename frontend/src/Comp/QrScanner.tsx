import {HealthItem} from "../Models/HealthItem";
import {Html5QrcodeScanner} from "html5-qrcode";
import {useEffect, useState} from "react";
import {Box, Center, useToast, Button} from "@chakra-ui/react";
import {useNavigate} from "react-router-dom";


export const QrScanner = () => {

    let navigate = useNavigate();
    const toast = useToast()
    const [scanResult, setScanResult] = useState<string>();

    function ShowToast() {
        return (
            toast({
                title: 'Account created.',
                description: "We've created your account for you.",
                status: 'success',
                duration: 9000,
                isClosable: true,
            })
        )
    }

    const go_to_item_page = (item_id: string) => {
        navigate("/item/" + item_id)
    }

    useEffect(() => {

        const scanner = new Html5QrcodeScanner('reader', {
            qrbox: {
                width: 250,
                height: 250,
            },
            fps: 30
        }, false)

        function success(result: string) {
            scanner.clear().then()
            go_to_item_page(result)
        }

        function error(err: any) {
            console.warn(err)
        }

        scanner.render(success, error)

    }, [])

    return (
        <Center>
            <Box
                width={600}
                height={600}
            >
                { scanResult
                    ? <>{scanResult}</>
                    : <div id="reader"></div>
                }
            </Box>
        </Center>
    )
}