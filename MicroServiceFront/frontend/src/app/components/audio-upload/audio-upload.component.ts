import { Component } from '@angular/core';
import { AudioService } from '../../services/audio.service';  // Assure-toi d'importer le service
import { VggService } from '../../services/vgg.service';  // Assure-toi d'importer le service

@Component({
  selector: 'app-audio-upload',
  templateUrl: './audio-upload.component.html',
  styleUrls: ['./audio-upload.component.css']
})
export class AudioUploadComponent {
  selectedFile: File | null = null;
  genrePrediction: string = '';

  selectedFileVgg: File | null = null;
  genrePredictionVgg: string = '';

  constructor(private audioService: AudioService,private vggService: VggService) {}

  // Méthode pour gérer la sélection du fichier
  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
    }
  }

  onFileSelectedVgg(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFileVgg = input.files[0];
      console.log(this.selectedFileVgg);

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
          // Handle different error cases
          alert('An error occurred while predicting the genre. Please try again later.');
        }
      );
    };
    reader.onerror = () => {
      console.error('Error reading file');
      alert('Error reading the selected file.');
    };
    reader.readAsDataURL(this.selectedFile);
  }

  sendAudioVgg() {
    if (!this.selectedFileVgg) return;
    console.log("passet");
    const reader = new FileReader();
    reader.onload = () => {
      const wavBase64 = (reader.result as string).split(',')[1];  // Extraction du Base64
      this.vggService.sendAudio(wavBase64).subscribe(
        (response) => {
          this.genrePredictionVgg = response.predicted_genre;
        },
        (error) => {
          console.error('Erreur:', error);
          // Handle different error cases
          alert('An error occurred while predicting the genre. Please try again later.');
        }
      );
    };
    reader.onerror = () => {
      console.error('Error reading file');
      alert('Error reading the selected file.');
    };
    reader.readAsDataURL(this.selectedFileVgg);
  }
  
}
