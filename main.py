from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

with open("universities.json", "r", encoding="utf-8") as f:
    universities = json.load(f)


@app.get("/universities")
async def get_universities():
    return universities


@app.get("/universities/name/{university_name}")
async def get_university_by_name(university_name: str):
    matching_universities = [u for u in universities if university_name.lower() in u["name"].lower()]

    if matching_universities:
        return matching_universities
    raise HTTPException(status_code=404, detail="No universities found with that name")


@app.get("/universities/{university_id}")
async def get_university_by_id(university_id: int):
    university = next((u for u in universities if u["id"] == university_id), None)

    if university:
        return university
    raise HTTPException(status_code=404, detail="University not found")


@app.get("/universities/region/{university_region}")
async def get_university_by_region(university_region: str):
    universities_in_region = [u for u in universities if u["region"].lower() == university_region.lower()]

    if universities_in_region:
        return universities_in_region
    raise HTTPException(status_code=404, detail="No universities found in this region")


@app.get("/universities/department/{university_department}")
async def get_university_by_department(university_department: str):
    universities_in_department = [u for u in universities if u["department"].lower() == university_department.lower()]

    if universities_in_department:
        return universities_in_department
    raise HTTPException(status_code=404, detail="No universities found in this department")


@app.get("/universities/city/{university_city}")
async def get_university_by_city(university_city: str):
    universities_in_city = [u for u in universities if u["city"].lower() == university_city.lower()]

    if universities_in_city:
        return universities_in_city
    raise HTTPException(status_code=404, detail="No universities found in this city")


@app.get("/universities/academy/{university_academy}")
async def get_university_by_academy(university_academy: str):
    universities_in_academy = [u for u in universities if u["academy"].lower() == university_academy.lower()]

    if universities_in_academy:
        return universities_in_academy
    raise HTTPException(status_code=404, detail="No universities found in this academy")


@app.get("/universities/type/{university_institution_type}")
async def get_university_by_type(university_institution_type: str):
    universities_in_institution_type = [
        u for u in universities
        if u["institution_type"].lower() == university_institution_type.lower()]

    if universities_in_institution_type:
        return universities_in_institution_type
    raise HTTPException(status_code=404, detail="No universities found in this institution type")
