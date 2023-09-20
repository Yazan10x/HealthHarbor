import {
    SimpleGrid,
    Box,
    Heading,
    Center, Spacer, Text
} from '@chakra-ui/react';
import {HealthItem} from "../Models/HealthItem";
import * as React from "react";
import { ItemCard } from '../Comp/ItemCard';
import { ItemAPI } from '../APIs/ItemAPI';
import {useEffect, useState} from "react";

export const Inventory = () => {

    const query_items = () => {
        ItemAPI.get_items("SELECT * FROM items").then((res) =>{
            setItems(res)
        })
    }
    
    const [items, setItems] = useState<HealthItem[] | undefined>(undefined);

    useEffect(() => {
        query_items()
    }, [])

    return (
        <>
            <Center>
                <Box>
                    <Text
                        textTransform={'uppercase'}
                        display="inline-block"
                        fontSize="20"
                        bgGradient="linear(to-r, brand.300, brand.200)"
                        backgroundClip="text"
                        p={2}
                        alignSelf={'flex-start'}
                        rounded={'md'}>
                        Inventory
                    </Text>
                    <Spacer height={20}/>
                </Box>
            </Center>
            <SimpleGrid  columns={[null, 1, 2]} spacing='20px'>
                {items?.map(item => <ItemCard _item={item}/>)}
            </SimpleGrid>
        </>
    );
}
