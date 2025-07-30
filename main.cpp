#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <curl/curl.h>

size_t write_data(void* ptr, size_t size, size_t nmemb, void* stream) {
    std::ofstream* out = static_cast<std::ofstream*>(stream);
    size_t total = size * nmemb;
    out->write(static_cast<char*>(ptr), total);
    return total;
}

std::string to_lower(const std::string& str) {
    std::string result;
    for (char c : str)
        result += std::tolower(c);
    return result;
}

bool is_uniprot_id(const std::string& id) {
    // Heuristic check: UniProt IDs are alphanumeric, often like P12345
    return id.length() >= 6 && std::isalpha(id[0]);
}

std::string make_url(const std::string& format, const std::string& id) {
    std::string lid = to_lower(id);

    if (format == "fasta") {
        if (is_uniprot_id(id)) {
            return "https://www.uniprot.org/uniprot/" + id + ".fasta";
        } else {
            return "https://www.rcsb.org/fasta/entry/" + lid;
        }
    } else if (format == "pdb" || format == "cif") {
        if (is_uniprot_id(id)) {
            return "https://alphafold.ebi.ac.uk/files/AF-" + id + "-F1-model_v4." + format;
        } else {
            return "https://files.rcsb.org/download/" + lid + "." + format;
        }
    }

    return "";
}

int download(const std::string& url, const std::string& output_path) {
    CURL* curl = curl_easy_init();
    if (!curl) {
        std::cerr << "curl init failed\n";
        return 1;
    }

    std::ofstream outfile(output_path, std::ios::binary);
    if (!outfile) {
        std::cerr << "failed to open file: " << output_path << "\n";
        return 1;
    }

    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &outfile);

    CURLcode res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    outfile.close();

    if (res != CURLE_OK) {
        std::cerr << "Download failed: " << curl_easy_strerror(res) << "\n";
        return 1;
    }

    std::cout << "Downloaded: " << output_path << "\n";
    return 0;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: danb <pdb|cif|fasta> <UniProtID|PDBID>\n";
        return 1;
    }

    std::string format = to_lower(argv[1]);
    std::string id = argv[2];

    if (format != "pdb" && format != "cif" && format != "fasta") {
        std::cerr << "Error: format must be 'pdb', 'cif', or 'fasta'\n";
        return 1;
    }

    std::string url = make_url(format, id);
    if (url.empty()) {
        std::cerr << "Could not generate URL\n";
        return 1;
    }

    std::string filename = id + "." + format;
    return download(url, filename);
}
