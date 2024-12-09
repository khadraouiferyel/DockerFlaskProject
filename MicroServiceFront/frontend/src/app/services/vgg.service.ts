import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VggService {
  private apiUrl = 'http://localhost:5002/predictVgg';

  constructor(private http: HttpClient) { }
  // Envoi des données Base64 au backend Flask
  sendAudio(wavBase64: string): Observable<any> {
    return this.http.post(this.apiUrl, { wav_music: wavBase64 });
  }
}
