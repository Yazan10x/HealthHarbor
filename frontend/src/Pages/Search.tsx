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
    Stack, Select, Spacer, HStack, Text, IconButton
} from '@chakra-ui/react';
import * as React from "react";
import { useState } from 'react';
import {CohereAPI} from "../APIs/CohereAPI";
import {MedicineEntry} from "../Models/MedicineEntries";
import {MedicineCard} from "../Comp/MedicineCard";
import {EditIcon} from "@chakra-ui/icons";

export const Search = () => {

    const [textArea, setTextArea] = useState<string>(''); // textArea input
    const [loading, setLoading] = useState<boolean>(false)
    const [submitted, setSubmitted] = useState<boolean>(false)
    const [medicineEntries, setMedicineEntries] = useState<Array<MedicineEntry>>()

    const onSubmit = () => {
        setLoading(true)
        setSubmitted(true)
        CohereAPI.get_medicine(textArea).then((res) => {
            setMedicineEntries(res)
            setLoading(false)
        })
    }

    const canSubmit = () => {
        return textArea === ''
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
                            Search for Medicine
                        </Heading>
                    </Box>
                    <Center>
                        <HStack>
                            <VStack>
                                <FormControl display='inline-block' width='60%' isDisabled={submitted}>
                                    <SimpleGrid columns={2} spacing={5} justifyContent='center'>
                                        <Box>
                                            <FormLabel display="inline-block" textAlign='center'>Age</FormLabel>
                                            <Input
                                                placeholder="Select Date and Time"
                                                fontSize="13px"
                                                type="date"
                                            />
                                        </Box>
                                        <Box>
                                            <FormLabel display="inline-block" textAlign='center'>Ethnicity</FormLabel>
                                            <Select placeholder='Select option'>
                                                <option value='option1'>Asian</option>
                                                <option value='option2'>Black/African</option>
                                                <option value='option3'>Hispanic/Latino/Latinx</option>
                                                <option value='option1'>Indigenous</option>
                                                <option value='option2'>Middle Eastern/North African</option>
                                                <option value='option3'>White/European</option>
                                                <option value='option3'>Other</option>
                                            </Select>
                                        </Box>
                                        <Box>
                                            <FormLabel display="inline-block" textAlign='center'>Height</FormLabel>
                                            <Select placeholder='Select option'>
                                                <option value='option1'>{"39cm <"}</option>
                                                <option value='option2'>{"40cm - 59cm"}</option>
                                                <option value='option2'>{"60cm - 79cm"}</option>
                                                <option value='option2'>{"80cm - 99cm"}</option>
                                                <option value='option2'>{"100cm - 119cm"}</option>
                                                <option value='option2'>{"120cm - 139cm"}</option>
                                                <option value='option2'>{"140cm - 159cm"}</option>
                                                <option value='option2'>{"160cm - 179cm"}</option>
                                                <option value='option2'>{"180cm - 199cm"}</option>
                                                <option value='option2'>{"200cm - 219cm"}</option>
                                                <option value='option2'>{"> 220cm"}</option>
                                            </Select>
                                        </Box>
                                        <Box>
                                            <FormLabel display="inline-block" textAlign='center'>Weight</FormLabel>
                                            <Select placeholder='Select option'>
                                                <option value='option1'>{"19kg <"}</option>
                                                <option value='option2'>{"20kg - 29kg"}</option>
                                                <option value='option2'>{"30kg - 39kg"}</option>
                                                <option value='option2'>{"40kg - 49kg"}</option>
                                                <option value='option2'>{"50kg - 59kg"}</option>
                                                <option value='option2'>{"60kg - 69kg"}</option>
                                                <option value='option2'>{"70kg - 79kg"}</option>
                                                <option value='option2'>{"80kg - 89kg"}</option>
                                                <option value='option2'>{"90kg - 99kg"}</option>
                                                <option value='option2'>{"100kg - 109kg"}</option>
                                                <option value='option2'>{"110kg - 119kg"}</option>
                                                <option value='option2'>{"120kg - 129kg"}</option>
                                                <option value='option2'>{"130kg - 139kg"}</option>
                                                <option value='option2'>{"140kg - 149kg"}</option>
                                                <option value='option2'>{"150kg - 159kg"}</option>
                                                <option value='option2'>{"> 160kg"}</option>
                                            </Select>
                                        </Box>
                                        <Box>
                                            <FormLabel display="inline-block" textAlign='center'>Sex</FormLabel>
                                            <RadioGroup>
                                                <Stack direction='row' display='flex' alignItems='center' justifyContent='space-evenly' >
                                                    <Radio value='1'>Male</Radio>
                                                    <Radio value='2'>Female</Radio>
                                                </Stack>
                                            </RadioGroup>
                                        </Box>
                                        <Box>
                                            <FormLabel display="inline-block" textAlign='center'>Pregnant</FormLabel>
                                            <RadioGroup>
                                                <Stack direction='row' display='flex' alignItems='center' justifyContent='space-evenly' >
                                                    <Radio value='3'>Yes</Radio>
                                                    <Radio value='4'>No</Radio>
                                                </Stack>
                                            </RadioGroup>
                                        </Box>
                                    </SimpleGrid>
                                    <Spacer height={"10px"}/>
                                    <FormLabel display="inline-block" textAlign='center'>Enter some symptoms:</FormLabel>
                                    <Textarea border='1px solid lightgrey' fontSize='12px' display='inline-block' placeholder='what are your symptoms?' value={textArea} onChange={(event) =>  setTextArea(event.target.value)} />
                                    <FormHelperText></FormHelperText>
                                </FormControl>
                                <FormControl>
                                    <Box marginTop='30px' textAlign='center'>
                                        <Button
                                            bgGradient="linear(to-r, brand.300, brand.200)"
                                            color="white"
                                            variant="solid"
                                            width='40%'
                                            textAlign='center'
                                            isLoading={loading}
                                            isDisabled={submitted || canSubmit()}
                                            onClick={onSubmit}>
                                            Submit
                                        </Button>
                                        { submitted
                                            ?
                                            <>
                                                <Spacer width={'5px'} height={'5px'}/>
                                                <IconButton
                                                    aria-label={''}
                                                    variant="solid"
                                                    width='15%'
                                                    textAlign='center'
                                                    isDisabled={false}
                                                    onClick={() => {
                                                        setSubmitted(false)
                                                        window.location.reload()
                                                    }}
                                                >
                                                    <EditIcon/>
                                                </IconButton>
                                            </>
                                            : <></>
                                        }
                                    </Box>
                                </FormControl>
                                <Spacer/>
                            </VStack>
                            <Spacer/>
                            { medicineEntries
                                ?
                                <VStack width={"500px"}>
                                    <MedicineCard entry={medicineEntries?.at(0)}></MedicineCard>
                                    <MedicineCard entry={medicineEntries?.at(1)}></MedicineCard>
                                    <MedicineCard entry={medicineEntries?.at(2)}></MedicineCard>
                                </VStack>
                                : <></>
                            }
                        </HStack>
                    </Center>

                </VStack>
            </Center>
        </>
    );
}
