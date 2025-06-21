import './globals.css';
import { Inter } from 'next/font/google';
import Provider from './provider';        // Auth0 + SWR config

export const metadata = { title: 'HomeEssentials' };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className={Inter({ subsets: ['latin'] }).className}>
        <Provider>{children}</Provider>
      </body>
    </html>
  );
}