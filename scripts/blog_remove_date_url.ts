/**
 * Translated from the `blog_remove_date_url.py` script using ChatGPT.
 * Not properly tested.
 */

import * as fs from 'fs-extra';
import * as path from 'path';

const blogPath: string = 'blog';

async function renameDirectories() {
    const firstLevelDirs: string[] = await fs.readdir(blogPath);

    for (const firstLevelDir of firstLevelDirs) {
        const yearDirPath: string = path.join(blogPath, firstLevelDir);
        const monthDirs: string[] = await fs.readdir(yearDirPath);

        for (const monthDir of monthDirs) {
            const blogPostDirPath: string = path.join(yearDirPath, monthDir);
            const newDirName: string = blogPostDirPath.split('-').slice(1).join('-'); // Remove `DD-` prefix
            const targetDirPath: string = path.join(blogPath, newDirName);

            await fs.move(blogPostDirPath, targetDirPath);
        }
    }

    // Remove first-level directories
    for (const firstLevelDir of firstLevelDirs) {
        await fs.rmdir(path.join(blogPath, firstLevelDir));
    }

    console.log('Directories renamed successfully.');
}

renameDirectories().catch(error => {
    console.error('Error:', error);
});
