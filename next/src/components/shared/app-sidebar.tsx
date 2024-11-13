import {
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarGroupContent,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
} from "@/components/ui/sidebar"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { ChefHat, CogIcon, HomeIcon, ShoppingBasket, Table } from "lucide-react"
import Image from "next/image"
import { Card } from "../ui/card"
// import { ModeToggle } from "../ModeToggle"

const sideBarLinks = [
    {
        title: "Dashboard",
        url: "/dashboard",
        icon: HomeIcon,
    },
    {
        title: "Menu",
        url: "/menu",
        icon: ChefHat,
    },
    {
        title: "Tables",
        url: "/tables",
        icon: Table,
    },
    {
        title: "Orders",
        url: "/orders",
        icon: ShoppingBasket,
    },
    {
        title: "Settings",
        url: "/settings",
        icon: CogIcon,
    },
]

export function AppSidebar() {  
    return (
        <Sidebar>
            <SidebarHeader>
                <SidebarMenu>
                    <Image
                        src="/logo.svg"
                        alt="logo"
                        width="100"
                        height="100" />
                </SidebarMenu>
            </SidebarHeader>
            <SidebarContent>
                <SidebarGroup>
                    {/* <SidebarGroupLabel>Application</SidebarGroupLabel> */}
                    <SidebarGroupContent>
                        <SidebarMenu>
                            {sideBarLinks.map((link) => (
                                <SidebarMenuItem key={link.title}>
                                    <SidebarMenuButton asChild>
                                        <a href={link.url}>
                                            <link.icon />
                                            <span>{link.title}</span>
                                        </a>
                                    </SidebarMenuButton>
                                </SidebarMenuItem>
                            ))}
                        </SidebarMenu>
                    </SidebarGroupContent>
                </SidebarGroup>
            </SidebarContent>
            <SidebarFooter className="flex flex-row items-center justify-between gap-1">
                <Card className="rounded-full flex-start p-2 gap-2">
                        <Avatar>
                            <AvatarImage src="https://github.com/shadcn.png" />
                            <AvatarFallback>
                                UN
                            </AvatarFallback>
                        </Avatar>
                        <div>
                            <h1 className="text-md font-bold">
                                user name
                            </h1>
                            <h3 className="text-xs font-light from-muted-foreground">
                                email@example.com
                            </h3>
                        </div>
                </Card>
                <div>
                    {/* <ModeToggle /> */}
                </div>  
            </SidebarFooter>
        </Sidebar>
    )
}
