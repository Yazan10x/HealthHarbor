'use client'

import {
    Container,
    SimpleGrid,
    Image,
    Flex,
    Heading,
    Text,
    Stack,
    StackDivider,
    Icon,
    useColorModeValue,
} from '@chakra-ui/react'
import { ReactElement } from 'react'
import {CalendarIcon, UnlockIcon} from "@chakra-ui/icons";
import {BiBrain} from "react-icons/all";

interface FeatureProps {
    text: string
    iconBg: string
    icon?: ReactElement
}

const Feature = ({ text, icon, iconBg }: FeatureProps) => {
    return (
        <Stack direction={'row'} align={'center'}>
            <Flex w={8} h={8} align={'center'} justify={'center'} rounded={'full'} bg={iconBg}>
                {icon}
            </Flex>
            <Text fontWeight={600}>{text}</Text>
        </Stack>
    )
}

export const OurStory = () => {
    return (
        <Container maxW={'5xl'} py={12}>
            <SimpleGrid columns={{ base: 1, md: 2 }} spacing={10}>
                <Stack spacing={4}>
                    <Text
                        textTransform={'uppercase'}
                        display="inline-block"
                        fontSize="20"
                        bgGradient="linear(to-r, brand.300, brand.200)"
                        backgroundClip="text"
                        p={2}
                        alignSelf={'flex-start'}
                        rounded={'md'}>
                        Our Story
                    </Text>
                    <Heading>Health Harbor - Hack The North Project</Heading>
                    <Text color={'gray.500'} fontSize={'lg'}>
                        Unlocking Health Wisdom: Your Symptoms, Your Solutions with HealthHarbor!
                    </Text>
                    <Text color={'gray.500'} fontSize={'lg'}>
                        We leveraged the power of Large Language Models (LLMs) to create HealthHarbor, a groundbreaking pharmaceutical inventory system. But what truly sets HealthHarbor apart?
                    </Text>
                    <Stack
                        spacing={4}
                        divider={
                            <StackDivider borderColor={useColorModeValue('gray.100', 'gray.700')} />
                        }>
                        <Feature
                            icon={<Icon as={CalendarIcon} color={'yellow.500'} w={5} h={5} />}
                            iconBg={useColorModeValue('yellow.100', 'yellow.900')}
                            text={'An efficient, scalable database that streamlines medication inventory management.\n'}
                        />
                        <Feature
                            icon={<Icon as={BiBrain} color={'green.500'} w={5} h={5} />}
                            iconBg={useColorModeValue('green.100', 'green.900')}
                            text={'A robust AI clustering system bolstered by our custom-trained Language Models (LLMs), enabling precise disease diagnosis and medication recommendations.\n'}
                        />
                        <Feature
                            icon={<Icon as={UnlockIcon} color={'purple.500'} w={5} h={5} />}
                            iconBg={useColorModeValue('purple.100', 'purple.900')}
                            text={'You can try it now'}
                        />
                    </Stack>
                </Stack>
                <Flex>
                    <Image
                        alt={'Picture of the team'}
                        src={
                            'about-us/htn-team.png'
                        }
                        objectFit={'contain'}
                        rounded={'5'}
                    />
                </Flex>
            </SimpleGrid>
        </Container>
    )
}