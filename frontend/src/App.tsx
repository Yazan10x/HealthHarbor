import * as React from "react"
import {
  ChakraProvider,
  extendTheme,
} from "@chakra-ui/react"
import {
  BrowserRouter,
  Routes,
  Route,
  useNavigate, Navigate
} from "react-router-dom";
import {Dashboard} from "./Pages/Dashboard/Dashboard";
import {NotFound} from "./Pages/Other/NotFound";
import {Home} from "./Pages/Home";
import {Search} from "./Pages/Search";
import {QrScanner} from "./Comp/QrScanner";
import {ItemCard} from "./Comp/ItemCard";
import {Inventory} from "./Pages/Inventory";
import {OurStory} from "./Pages/Other/OurStory";

const theme = extendTheme({
  initialColorMode: 'dark',
  colors: {
    // https://colorhunt.co/palette/27005d9400ffaed2ffe4f1ff
    brand: {
      100: "#27005D",

      200: "#9400FF",

      300: "#AED2FF",

      400: "#E4F1FF",
    },
  },
})

export const App = () => (
    <ChakraProvider theme={theme}>
      <BrowserRouter>
        <Routes>

        <Route path="/" element={<Dashboard/>}>
          <Route path="/search" element={<Search/>}/>
          <Route path="/scanner" element={<QrScanner/>}/>
          <Route path="/inventory" element={<Inventory/>}/>
          <Route path="/inventory/:item_id" element={<ItemCard/>}/>
          <Route path="/our-story" element={<OurStory/>}/>
        </Route>

          <Route path="*" element={<NotFound/>}/>

        </Routes>
      </BrowserRouter>
    </ChakraProvider>
)
