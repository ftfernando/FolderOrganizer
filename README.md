# Folder Organizer Documentation

- [English Version](#english-version)
- [Versão em Português](#versão-em-português)



## English Version
<!-- English Version -->

<p align="center">
  <img src="https://github.com/user-attachments/assets/62bbd0f1-bede-45b8-a7c0-0981b6042749" alt="Folders">
</p>

---

<h1>Folder Organizer</h1>

The Organizer App is designed to streamline file management by automatically sorting and organizing files into designated folders. This tool offers an intuitive interface built with Tkinter, which allows users to:

- **Automatic File Organization:** Files are categorized based on their extensions or name prefixes. The app supports a variety of file types, like:
  - **Images:** jpg, jpeg, png, gif, svg, bmp, tiff
  - **Documents:** pdf, doc, docx, txt, rtf, odt, docm
  - **Audio Files:** mp3, wav, flac, aac, ogg, opus
  - **Videos:** mp4, avi, mkv, mov, wmv, flv, webm
  - **Ebooks:** epub, mobi, azw3, pdb, fb2

- **Backup Functionality:** Each file is backed up to a designated backup folder before being moved, ensuring that original files are preserved.

- **Customizable Configuration:** The app reads settings from a `controller.json` file, allowing users to define:
  - **Extension Mappings:** Determine which types of files go into specific folders.
  - **Name Prefix Mappings:** Files with certain prefixes are moved to predefined folders. For example, files starting with "work_" or "job_" are sorted into the "work_folder."
  - **Ignored Folders:** Specify folders that should be excluded from processing. The app skips these directories, ensuring that their contents remain untouched during the file organization process.

- **Logging:** Detailed logs of file operations are stored in a specified log folder for tracking and troubleshooting.

The app simplifies file management tasks, making it easy for users to keep their digital workspace organized with minimal effort.

---

<h2>Usage</h2>

<p align="center">
  <img src="https://github.com/user-attachments/assets/185f6fa3-aa66-4bdf-8702-696cea9a25e8" alt="GUI">
</p>

1. **Run the Application:**
   Start the application by running the script:
   ```bash
   python file_organizer.py
   ```
   
2. **Select the Main Folder:**
   Use the "Browse" button to select the folder you want to organize.
3. **Start Processing:**
Click "Start Processing" to begin organizing your files based on the configuration.


---

<h2>Config</h2>

The <a href='controller.json' style='text-decoration:none; color:inherit'>controller.json</a> file defines how files are organized and managed within the application. 

This configuration file allows you to specify mappings for file extensions and name prefixes, as well as folders to be ignored during the organization process.

**Example `controller.json` Configuration:**

```json
{
    "extension_mapping": {
        "jpg,jpeg,png,gif,svg,bmp,tiff": "images_folder",
        "pdf,doc,docx,txt,rtf,odt,docm": "documents_folder",
        "mp3,wav,flac,aac,ogg,opus": "audio_folder",
        "mp4,avi,mkv,mov,wmv,flv,webm": "videos_folder",
        "epub,mobi,azw3,pdb,fb2": "ebooks_folder"
    },

    "name_prefix_mapping": {
        "work_": "work_folder",
        "job_": "work_folder"
    },

    "ignore_folders": ["backup_folder", "ignore"]
}

```

---
<h2> Final Considerations </h2>

Feel free to adjust any details as needed!

If you have any questions, tips, want to share experiences, or just chat, feel free to reach out to me on any of my social networks!

<h3>Social Media</h3>
<ul>
    <li>
        <i class="fab fa-linkedin"></i>
        <a href="https://www.linkedin.com/in/fernandofthompson/" target="_blank">
            LinkedIn
        </a>
    </li>
    <li>
        <i class="fab fa-instagram"></i>
        <a href="https://www.instagram.com/f.fthompson/" target="_blank">
            Instagram
        </a>
    </li>
</ul>


---
## Versão em Português
<!-- Versão em Português -->

<p align="center">
  <img src="https://github.com/user-attachments/assets/62bbd0f1-bede-45b8-a7c0-0981b6042749" alt="Folders">
</p>

---

# Organizador de Pastas

O Aplicativo Organizador é projetado para simplificar a gestão de arquivos, organizando-os automaticamente em pastas designadas. Esta ferramenta oferece uma interface intuitiva construída com Tkinter, que permite aos usuários:

- **Organização Automática de Arquivos:** Arquivos são categorizados com base em suas extensões ou prefixos de nomes. O aplicativo suporta uma variedade de tipos de arquivos, como:
  - **Imagens:** jpg, jpeg, png, gif, svg, bmp, tiff
  - **Documentos:** pdf, doc, docx, txt, rtf, odt, docm
  - **Arquivos de Áudio:** mp3, wav, flac, aac, ogg, opus
  - **Vídeos:** mp4, avi, mkv, mov, wmv, flv, webm
  - **Ebooks:** epub, mobi, azw3, pdb, fb2

- **Funcionalidade de Backup:** Cada arquivo é salvo em uma pasta de backup designada antes de ser movido, garantindo que os arquivos originais sejam preservados.

- **Configuração Personalizável:** O aplicativo lê as configurações de um arquivo `controller.json`, permitindo aos usuários definir:
  - **Mapeamentos de Extensões:** Determinar quais tipos de arquivos vão para pastas específicas.
  - **Mapeamentos de Prefixos de Nome:** Arquivos com certos prefixos são movidos para pastas pré-definidas. Por exemplo, arquivos que começam com "work_" ou "job_" são classificados na "work_folder."
  - **Pastas Ignoradas:** Especificar pastas que devem ser excluídas do processamento. O aplicativo ignora essas diretórios, garantindo que seu conteúdo permaneça intocado durante o processo de organização de arquivos.

- **Registro de Logs:** Logs detalhados das operações de arquivos são armazenados em uma pasta de logs especificada para rastreamento e solução de problemas.

O aplicativo simplifica as tarefas de gerenciamento de arquivos, facilitando para os usuários manter seu espaço de trabalho digital organizado com o mínimo de esforço.

---

## Uso

<p align="center">
  <img src="https://github.com/user-attachments/assets/185f6fa3-aa66-4bdf-8702-696cea9a25e8" alt="GUI">
</p>

1. **Execute o Aplicativo:**
   Inicie o aplicativo executando o script:
   ```bash
   python file_organizer.py
   ```
2. **Selecione a Pasta Principal:**
Use o botão "Browse" para selecionar a pasta que você deseja organizar.
3. **Inicie o Processamento:**
Clique em "Start Processing" para começar a organizar seus arquivos com base na configuração.

---

<h2>Configuração</h2>

O arquivo <a href='controller.json' style='text-decoration:none; color:inherit'>controller.json</a> define como os arquivos são organizados e gerenciados dentro do aplicativo.

Este arquivo de configuração permite que você especifique mapeamentos para extensões de arquivos e prefixos de nomes, bem como pastas a serem ignoradas durante o processo de organização.

Exemplo de Configuração do `controller.json`:

```
{
    "extension_mapping": {
        "jpg,jpeg,png,gif,svg,bmp,tiff": "images_folder",
        "pdf,doc,docx,txt,rtf,odt,docm": "documents_folder",
        "mp3,wav,flac,aac,ogg,opus": "audio_folder",
        "mp4,avi,mkv,mov,wmv,flv,webm": "videos_folder",
        "epub,mobi,azw3,pdb,fb2": "ebooks_folder"
    },

    "name_prefix_mapping": {
        "work_": "work_folder",
        "job_": "work_folder"
    },

    "ignore_folders": ["backup_folder", "ignore"]
}
```

---
<h2> Considerações Finais </h2>

Sinta-se à vontade para ajustar quaisquer detalhes conforme necessário!

Se você tiver alguma dúvida, dica, quiser compartilhar experiências ou apenas conversar, fique à vontade para entrar em contato comigo em qualquer uma das minhas redes sociais!

<h3>Redes Sociais</h3>
<ul>
    <li>
        <i class="fab fa-linkedin"></i>
        <a href="https://www.linkedin.com/in/fernandofthompson/" target="_blank">
            LinkedIn
        </a>
    </li>
    <li>
        <i class="fab fa-instagram"></i>
        <a href="https://www.instagram.com/f.fthompson/" target="_blank">
            Instagram
        </a>
    </li>
</ul>
