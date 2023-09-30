import {Treatment} from "../Models/Treatment";
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
    Badge, Link
} from '@chakra-ui/react'
import {useNavigate, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import {TreatmentAPI} from "../APIs/TreatmentAPI";
import * as React from "react";
import {MedicineEntry} from "../Models/MedicineEntries";

interface Props {
    entry: MedicineEntry | undefined
}


export const MedicineCard = ({entry}: Props) => {



    const [item, setItem] = useState<Treatment | undefined>(undefined);

    const get_item = () => {
        TreatmentAPI.get_treatment_by_label(entry!.medicine).then((res) =>{
            setItem(res)
        })
        // ItemAPI.get_item("6c39313e-5500-11ee-8c99-0242ac120002").then((res) =>{
        //     setItem(res)
        // })
    }

    useEffect(() => {
        get_item()
    }, [])

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
                        maxH={{ base: '100%', sm: '200px' }}
                        src={item.image_url}
                        alt={item.image_url}
                    />

                    <Stack>
                        <CardBody>
                            <Link
                                onClick={() => {
                                    window.location.pathname = '/inventory/' + item?.id
                                }}
                            >
                                <Heading
                                    size='md'
                                    as='u'
                                >
                                    {item?.label}
                                </Heading>
                            </Link>

                            <HStack>
                                <Badge colorScheme={'purple'}>{"Diseases: " + entry?.disease}</Badge>
                                <Badge colorScheme={'red'}>{"Confidence: " + entry?.confidence.toFixed(2) + "%"}</Badge>
                            </HStack>
                            <Text py='2'>
                                {item.description}
                            </Text>
                        </CardBody>
                    </Stack>
                </Card>
                :
                <Stack>
                    <Spacer/>
                    <Skeleton height='100px'/>
                    <Skeleton height='100px'/>
                </Stack>
            }
        </>
    )
}
