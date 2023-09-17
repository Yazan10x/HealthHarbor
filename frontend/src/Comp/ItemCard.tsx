import {HealthItem} from "../Models/HealthItem";
import {
    Card,
    HStack,
    Spacer,
    CardBody,
    CardFooter,
    Image,
    Center,
    Stack,
    Heading,
    Text,
    Button,
    Skeleton,
    useToast,
    Badge
} from '@chakra-ui/react'
import {useNavigate, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import {ItemAPI} from "../APIs/ItemAPI";
import * as React from "react";

interface Props {
    _item_id?: string | undefined
}


export const ItemCard = ({_item_id}: Props) => {

    let {item_id} = useParams();
    let final_item_id: string;

    if (_item_id) {
        final_item_id = _item_id
    } else {
        final_item_id = item_id!
    }

    const [item, setItem] = useState<HealthItem | undefined>(undefined);
    const toast = useToast()

    const get_item = () => {
        ItemAPI.get_item(final_item_id!).then((res) =>{
            setItem(res)
            if (item_id) {
                toast({
                    title: 'QR Code Scanned',
                    description: "We are searching for you.",
                    status: 'success',
                    duration: 5000,
                    isClosable: true,
                })
            }
        })
    }

    const update_quantity = (q: number) => {
        item!.quantity += q
        ItemAPI.update_item(item!).then((res) => {
            setItem(res)
            toast({
                title: 'Item update successfully',
                status: 'success',
                duration: 5000,
                isClosable: true,
            })
        })
    }

    useEffect(() => {
        get_item()
    }, [])

    return (
        <>
            {item_id
                ? <>
                    <Center>
                        <Heading
                            display="inline-block"
                            as="h2"
                            size="md"
                            bgGradient="linear(to-r, brand.300, brand.200)"
                            backgroundClip="text">
                            Health Harbor - Single Item View
                        </Heading>
                        <Spacer height={20}/>
                    </Center>
                </>
                :
                <></>
            }
            { item ?
                <Card
                    direction={{ base: 'column', sm: 'row' }}
                    overflow='hidden'
                    variant='outline'
                >
                    <Image
                        objectFit='cover'
                        maxW={{ base: '100%', sm: '200px' }}
                        src={item.url}
                        alt={item.url}
                    />

                    <Stack>
                        <CardBody>
                            <Heading size='md'>{item?.label}</Heading>

                            <Badge colorScheme={'purple'}>{"Quantity: " + item.quantity}</Badge>
                            <Text py='2'>
                                {item.description}
                            </Text>

                        </CardBody>

                        <CardFooter>
                            <HStack>
                                <Button
                                    bgGradient="linear(to-r, brand.300, brand.200)"
                                    color="white"
                                    variant="solid"
                                    isDisabled={item.quantity <= 0}
                                    onClick={() => {update_quantity(-1)}}
                                >
                                    Check out
                                </Button>
                                <Button
                                    bgGradient="linear(to-r, brand.200, brand.100)"
                                    color="white"
                                    variant="solid"
                                    onClick={() => {update_quantity(1)}}
                                >
                                    Check in
                                </Button>
                            </HStack>
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
                </Stack>
            }
        </>
    )
}
