import type { Metadata } from "next";
import localFont from "next/font/local";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/shared/app-sidebar"
import "./globals.css";
// import { ThemeProvider } from "@/lib/theme-provider";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "Restaurant point of sale management system",
  description: "Advanced restaurant point of sale management system",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {/* <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        > */}
        <SidebarProvider>
          <AppSidebar />
          <main className="px-2 w-full">
            <SidebarTrigger />
            {children}
          </main>
          </SidebarProvider>
          {/* </ThemeProvider> */}
      </body>
    </html>
  );
}
