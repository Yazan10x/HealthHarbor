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
    Button,
    Radio, 
    RadioGroup,
    Stack,
} from '@chakra-ui/react';
import * as React from "react";
import { useState } from 'react';
import './Search.css'


interface Props {
}

export const Search = () => {

    const [textArea, setTextArea] = useState<string>(''); // textArea input
    const [genderValue, setGenderValue] = React.useState('0') // radio buttons
    const [pregnantValue, setPregnantValue] = React.useState('0') // radio buttons


    const onSubmit = () => {
        console.log(textArea)
    }

    return (
        <>
            <Center>
                
                <VStack
                    width='100%'
                    spacing={10}
                    align='center'
                >
                    <Box>
                        <Heading
                            display="inline-block"
                            as="h2"
                            size="lg"
                            bgGradient="linear(to-r, brand.300, brand.200)"
                            backgroundClip="text">
                            Search
                        </Heading>
                    </Box>

                    <FormControl display='inline-block' width='60%'>
                        <FormLabel display="inline-block" textAlign='center'>Enter some symptoms:</FormLabel>
                        <Textarea border='1px solid lightgrey' fontSize='12px' display='inline-block' placeholder='what are your symptoms?' value={textArea} onChange={(event) =>  setTextArea(event.target.value)} />
                        <FormHelperText></FormHelperText>
                    </FormControl>

                    <FormControl display='inline-block' width='100%'>
                        <SimpleGrid columns={2} spacing={5} justifyContent='center'>
                            <Box>
                                <FormLabel display="inline-block" textAlign='center'>Age</FormLabel>
                                <Input type='text' className='labelText' ></Input>
                            </Box>
                            <Box>
                                <FormLabel display="inline-block" textAlign='center'>Ethnicity</FormLabel>
                                <Input type='text'></Input>
                            </Box>
                            <Box>
                                <FormLabel display="inline-block" textAlign='center'>Height</FormLabel>
                                <Input type='text'></Input>
                            </Box>
                            <Box>
                                <FormLabel display="inline-block" textAlign='center'>Weight</FormLabel>
                                <Input type='text'></Input>
                            </Box>
                            <Box>
                                <FormLabel display="inline-block" textAlign='center'>Gender</FormLabel>
                                <RadioGroup onChange={setGenderValue} value={genderValue}>
                                    <Stack direction='row' display='flex' alignItems='center' justifyContent='space-evenly' >
                                        <Radio value='1'>Male</Radio>
                                        <Radio value='2'>Female</Radio>
                                    </Stack>
                                </RadioGroup>
                            </Box>
                            <Box>
                                <FormLabel display="inline-block" textAlign='center'>Pregnant</FormLabel>
                                <RadioGroup onChange={setPregnantValue} value={pregnantValue}>
                                    <Stack direction='row' display='flex' alignItems='center' justifyContent='space-evenly' >
                                        <Radio value='3'>Yes</Radio>
                                        <Radio value='4'>No</Radio>
                                    </Stack>
                                </RadioGroup>   
                            </Box>
                        </SimpleGrid>

                    
                        <Box marginTop='30px' textAlign='center'>
                            <Button display='inline-block' width='50%' textAlign='center' onClick={onSubmit}>
                                Submit
                            </Button>
                        </Box>
                    </FormControl>

                </VStack>
            </Center>
        </>
    );
}
