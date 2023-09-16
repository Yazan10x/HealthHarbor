import {
    Box,
    Heading,
    Center,
    VStack,
    SimpleGrid,

} from '@chakra-ui/react';
import * as React from "react";

interface Props {
}

export const Home = () => {


    return (
        <>
            <Center>
                <VStack
                    spacing={10}
                    align='stretch'
                >
                    <Box>
                        <Heading
                            display="inline-block"
                            as="h2"
                            size="md"
                            bgGradient="linear(to-r, brand.300, brand.200)"
                            backgroundClip="text">
                            Health Harbor
                        </Heading>
                    </Box>
                    <Box>
                        <SimpleGrid  columns={[null, 1]} spacing='20px'>

                        </SimpleGrid>
                    </Box>
                </VStack>
            </Center>
        </>
    );
}
