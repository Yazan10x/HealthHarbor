import {
    SimpleGrid
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
            <SimpleGrid  columns={[null, 1, 3]} spacing='20px'>
                {items?.map(item => <ItemCard _item_id={`${item.id}`}/>)}
            </SimpleGrid>
        </>
    );
}
