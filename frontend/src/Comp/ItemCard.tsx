import {HealthItem} from "../Models/HealthItem";
import {
    Card,
    HStack,
    Spacer,
    CardBody,
    CardFooter,
    Image,
    Stack,
    Heading,
    Text,
    Button,
    Skeleton,
    useToast
} from '@chakra-ui/react'
import {useNavigate, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import {ItemAPI} from "../APIs/ItemAPI";


export const ItemCard = () => {

    let {item_id} = useParams();
    const [item, setItem] = useState<HealthItem>();
    const toast = useToast()

    function ShowToast() {
        return (
            toast({
                title: 'QR Code Scanned',
                description: "We are searching for you.",
                status: 'success',
                duration: 9000,
                isClosable: true,
            })
        )
    }

    const get_item = () => {
        ItemAPI.get_item(item_id!).then((res) =>{
            setItem(res)
        })
    }

    useEffect(() => {
        // get_item()
    })

    return (
        <>
            { item ?
                <Card
                    direction={{ base: 'column', sm: 'row' }}
                    overflow='hidden'
                    variant='outline'
                >
                    <Image
                        objectFit='cover'
                        maxW={{ base: '100%', sm: '200px' }}
                        src='https://img.freepik.com/premium-vector/3d-medicine-icon-vector-isolated-white-background-3d-pharmacy-medical-healthcare-concept-cartoon-minimal-style-3d-drug-icon-vector-render-illustration_726846-5915.jpg?w=2000'
                        alt='Medicine'
                    />

                    <Stack>
                        <CardBody>
                            <Heading size='md'>{}</Heading>

                            <Text py='2'>
                                Caffè latte is a coffee beverage of Italian origin made with espresso
                                and steamed milk.
                            </Text>
                        </CardBody>

                        <CardFooter>
                            <Button variant='solid' colorScheme='blue'>
                                Buy Latte
                            </Button>
                        </CardFooter>
                    </Stack>
                </Card>
                :
                <Stack>
                    <Spacer/>
                    <HStack>
                        <Skeleton height='100px' width={"100%"}/>
                        <Skeleton height='100px' width={"100%"}/>
                    </HStack>
                    <Skeleton height='200px' width={"100%"}/>
                    <HStack>
                        <Skeleton height='100px' width={"100%"}/>
                        <Skeleton height='100px' width={"100%"}/>
                        <Skeleton height='100px' width={"100%"}/>
                    </HStack>
                    <Skeleton height='100px' width={"100%"}/>
                    {ShowToast()}
                </Stack>
            }
        </>
    )
}