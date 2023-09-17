import {
    SimpleGrid,
    Box,
    Heading,
    Center, Spacer
} from '@chakra-ui/react';
import {HealthItem} from "../Models/HealthItem";
import * as React from "react";
import { ItemCard } from '../Comp/ItemCard';
import { ItemAPI } from '../APIs/ItemAPI';
import {useEffect, useState} from "react";

interface Props {
}

export const Items = () => {

    const query_items = () => {
        ItemAPI.get_items("SELECT * FROM items").then((res) =>{
            console.log(res)
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
                    <Heading
                        display="inline-block"
                        as="h2"
                        size="lg"
                        bgGradient="linear(to-r, brand.300, brand.200)"
                        backgroundClip="text">
                        Items
                    </Heading>
                    <Spacer height={20}/>
                </Box>
            </Center>
            <SimpleGrid  columns={[null, 1, 2]} spacing='20px'>
                {items?.map(item => <ItemCard _item_id={`${item.id}`}/>)}
            </SimpleGrid>
        </>
    );
}
