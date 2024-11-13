import { Component } from '@angular/core';
import { AudioService } from '../../services/audio.service';  // Assure-toi d'importer le service

@Component({
  selector: 'app-audio-upload',
  templateUrl: './audio-upload.component.html',
  styleUrls: ['./audio-upload.component.css']
})
export class AudioUploadComponent {
  selectedFile: File | null = null;
  genrePrediction: string = '';

  constructor(private audioService: AudioService) {}

  // Méthode pour gérer la sélection du fichier
  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
    }
  }

  // Méthode pour envoyer le fichier au backend Flask
  sendAudio() {
    if (!this.selectedFile) return;

    const reader = new FileReader();
    reader.onload = () => {
      const wavBase64 = (reader.result as string).split(',')[1];  // Extraction du Base64
      this.audioService.sendAudio(wavBase64).subscribe(
        (response) => {
          this.genrePrediction = response.predicted_genre;
        },
        (error) => {
          console.error('Erreur:', error);
        }
      );
    };
    reader.readAsDataURL(this.selectedFile);
  }
}
