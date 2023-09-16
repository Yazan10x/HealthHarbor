import {
    Box,
    Heading,
    Center,
    VStack,
    SimpleGrid,
    FormControl,
    FormLabel,
    FormErrorMessage,
    FormHelperText,
    Input,
    Textarea,

} from '@chakra-ui/react';
import * as React from "react";

interface Props {
}

export const Search = () => {
    return (
        <>
            <Center>
                <VStack
                    spacing={10}
                    align='center'
                >
                    <Box>
                        <Heading
                            display="inline-block"
                            as="h2"
                            size="md"
                            bgGradient="linear(to-r, brand.300, brand.200)"
                            backgroundClip="text">
                            Search
                        </Heading>
                    </Box>

                    <FormControl display='inline-block'>
                        <FormLabel display="inline-block">Enter some symptoms:</FormLabel>
                        <Textarea border='1px solid lightgrey' fontSize='12px' display='inline-block' placeholder='' />
                        <FormHelperText></FormHelperText>
                    </FormControl>

                </VStack>
            </Center>
        </>
    );
}
